#!/usr/bin/env python3
from PIL import Image, ImageDraw, ImageFont
import os

# Create images directory if it doesn't exist
os.makedirs('.', exist_ok=True)

# Blog images to create
blog_images = {
    'nvidia.jpg': ('NVIDIA', '#76B900', 'The Inspiring Journey'),
    'bill-gates.jpg': ('Bill Gates', '#0078D4', 'Computing Visionary'),
    'blackrock.jpg': ('BlackRock', '#000000', 'Investment Giant'),
    'ola.jpg': ('Ola', '#FF6B35', 'Revolutionizing Mobility'),
    'intel.jpg': ('Intel', '#0071C5', 'Rise and Fall'),
    'reliance-jio.jpg': ('Reliance Jio', '#FF6B00', 'Digital India'),
    'zoho.jpg': ('Zoho', '#FF6B35', 'Cloud Software Excellence'),
    'lenskart.jpg': ('Lenskart', '#00BFA5', 'Vision Revolution'),
    'larry-ellison.jpg': ('Larry Ellison', '#FF5722', 'Oracle Legend'),
    'zerodha.jpg': ('Zerodha', '#FF6B35', 'Trading Revolution'),
    'elon-musk.jpg': ('Elon Musk', '#E31E24', 'Innovation Leader'),
    'steve-jobs.jpg': ('Steve Jobs', '#000000', 'Apple Visionary'),
    'startup-funding.jpg': ('Startup Funding', '#4CAF50', 'Investment Guide'),
    'business-plan.jpg': ('Business Plan', '#2196F3', 'Strategic Planning'),
    'market-research.jpg': ('Market Research', '#FF9800', 'Data Insights'),
    'customer-validation.jpg': ('Customer Validation', '#9C27B0', 'Product-Market Fit'),
    'mvp-development.jpg': ('MVP Development', '#00BCD4', 'Minimum Viable Product'),
    'pitch-deck.jpg': ('Pitch Deck', '#E91E63', 'Investor Presentation'),
    'lean-startup.jpg': ('Lean Startup', '#8BC34A', 'Agile Methodology'),
    'product-development.jpg': ('Product Development', '#3F51B5', 'Building Products'),
    'competitor-analysis.jpg': ('Competitor Analysis', '#FF5722', 'Market Intelligence'),
    'digital-marketing.jpg': ('Digital Marketing', '#607D8B', 'Online Strategies'),
    'content-marketing.jpg': ('Content Marketing', '#795548', 'Storytelling'),
    'brand-building.jpg': ('Brand Building', '#9E9E9E', 'Brand Identity')
}

def create_blog_image(filename, title, color, subtitle):
    # Create image
    img = Image.new('RGB', (800, 600), color)
    draw = ImageDraw.Draw(img)
    
    # Try to use a default font, fallback to basic if not available
    try:
        title_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 60)
        subtitle_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 30)
    except:
        title_font = ImageFont.load_default()
        subtitle_font = ImageFont.load_default()
    
    # Calculate text positions
    title_bbox = draw.textbbox((0, 0), title, font=title_font)
    title_width = title_bbox[2] - title_bbox[0]
    title_height = title_bbox[3] - title_bbox[1]
    
    subtitle_bbox = draw.textbbox((0, 0), subtitle, font=subtitle_font)
    subtitle_width = subtitle_bbox[2] - subtitle_bbox[0]
    subtitle_height = subtitle_bbox[3] - subtitle_bbox[1]
    
    # Center the text
    title_x = (800 - title_width) // 2
    title_y = (600 - title_height - subtitle_height - 20) // 2
    
    subtitle_x = (800 - subtitle_width) // 2
    subtitle_y = title_y + title_height + 20
    
    # Draw text with white color
    draw.text((title_x, title_y), title, fill='white', font=title_font)
    draw.text((subtitle_x, subtitle_y), subtitle, fill='white', font=subtitle_font)
    
    # Save image
    img.save(filename)
    print(f"Created {filename}")

# Create all blog images
for filename, (title, color, subtitle) in blog_images.items():
    create_blog_image(filename, title, color, subtitle)

print("All blog images created successfully!")