import pygame
import random
import math

# ตั้งค่าเริ่มต้น Pygame
pygame.init()
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Colorful Flower with Moon & Twinkling Stars")
clock = pygame.time.Clock()

# --- สีต่างๆ ---
BLACK = (10, 10, 25) # พื้นหลังท้องฟ้ากลางคืน
MOON_COLOR = (240, 240, 210) # สีพระจันทร์นวลๆ
MOON_GLOW = (255, 255, 200, 50)

# --- ละอองดาวระยิบระยับ (Twinkling Stars) ---
stars = []
for _ in range(120):
    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT)
    size = random.uniform(1.0, 2.5)
    brightness = random.uniform(50, 255)
    speed = random.uniform(1.5, 4.0)
    stars.append([x, y, size, brightness, speed])

# --- ฟังก์ชั่นวาดพระจันทร์เสี้ยวดวงเล็กๆ ---
def draw_small_crescent_moon(surface, x, y, radius):
    # วาดดวงจันทร์หลัก
    pygame.draw.circle(surface, MOON_COLOR, (x, y), radius)
    # วาดวงกลมสีเดียวกับพื้นหลังซ้อนเพื่อสร้างเงาสี้ยว
    pygame.draw.circle(surface, BLACK, (x + int(radius * 0.5), y - int(radius * 0.2)), radius)

# --- ฟังก์ชั่นวาดดอกไม้เน้นสีสันสวยงาม (Colorful Flower) ---
def draw_colorful_flower(surface, cx, cy, t):
    # 1. วาดลำต้น (Stem)
    pygame.draw.line(surface, (50, 205, 50), (cx, cy + 150), (cx, cy), 6)
    
    # 2. วาดใบไม้ (Leaves)
    pygame.draw.ellipse(surface, (34, 139, 34), (cx - 40, cy + 60, 45, 20))
    pygame.draw.ellipse(surface, (34, 139, 34), (cx - 5, cy + 40, 45, 20))

    # 3. วาดกลีบดอกไม้สีสันสดใสไล่เฉด (Petals)
    num_petals = 12
    petal_length = 70 + math.sin(t * 0.05) * 5 # ให้กลีบขยับพลิ้วไหวเล็กน้อย
    
    for i in range(num_petals):
        angle = i * (2 * math.pi / num_petals)
        px = cx + math.cos(angle) * petal_length
        py = cy + math.sin(angle) * petal_length
        
        # เปลี่ยนสีกลีบดอกเป็นแบบสเปกตรัม/สีสดใสตามมุม
        r = int((math.sin(angle + t * 0.02) + 1) * 120 + 15)
        g = int((math.cos(angle * 2) + 1) * 100 + 50)
        b = int((math.sin(angle * 3) + 1) * 120 + 15)
        
        pygame.draw.line(surface, (r, g, b), (cx, cy), (px, py), 4)
        pygame.draw.circle(surface, (min(r + 30, 255), min(g + 30, 255), min(b + 30, 255)), (int(px), int(py)), 8)

    # 4. เกสรดอกไม้ฉายแสงเปล่งประกาย
    pygame.draw.circle(surface, (255, 215, 0), (cx, cy), 18)
    pygame.draw.circle(surface, (255, 255, 180), (cx, cy), 10)

# --- Main Loop ---
running = True
frame_count = 0

while running:
    clock.tick(60)
    frame_count += 1
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 1. ล้างหน้าจอด้วยสีท้องฟ้า
    screen.fill(BLACK)

    # 2. วาดละอองดาวระยิบระยับ (Twinkling Effect)
    for star in stars:
        # ปรับความสว่างแบบระยิบระยับ
        star[3] += star[4]
        if star[3] > 255 or star[3] < 50:
            star[4] = -star[4]
        
        alpha_color = (int(star[3]), int(star[3]), min(255, int(star[3] + 50)))
        pygame.draw.circle(screen, alpha_color, (int(star[0]), int(star[1])), int(star[2]))

    # 3. วาดพระจันทร์ดวงเล็กๆ บริเวณมุมขวาบน
    draw_small_crescent_moon(screen, x=650, y=150, radius=25)

    # 4. วาดดอกไม้ตรงกลางพร้อมปรับสีสันสดใส
    draw_colorful_flower(screen, WIDTH // 2, HEIGHT // 2 + 50, frame_count)

    # อัปเดตหน้าจอ
    pygame.display.flip()

pygame.quit()
