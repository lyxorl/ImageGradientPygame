import pygame
import sys

def load_image(path):
    img = pygame.image.load(path).convert_alpha()
    return img

def save_image(surface, path):
    pygame.image.save(surface, path)

def blend_color(origin_color, color_with_alpha):

    alpha = color_with_alpha[3]/255.0
    inv_alpha = 1-alpha

    r = int(origin_color[0] * inv_alpha + color_with_alpha[0] * alpha)
    g = int(origin_color[1] * inv_alpha + color_with_alpha[1] * alpha)
    b = int(origin_color[2] * inv_alpha + color_with_alpha[2] * alpha)
    
    return (r, g, b)

def add_gradient(surface, color_limit, side, size):
    #to test
    if (side == "top"):
        for k in range(size):
            for j in range(surface.get_width()):
                pixel = blend_color(surface.get((j,k)),(color_limit[0],color_limit[1],color_limit[2],255-((k/size)*255)))
                surface.set_at((j,k), pixel)

    if (side == "bottom"):
        for k in range(size):
            for j in range(surface.get_width()):
                pixel = blend_color(surface.get_at((j,surface.get_height()-k)),(color_limit[0],color_limit[1],color_limit[2],255-((k/size)*255)))
                surface.set_at((j,surface.get_height()-k), pixel)

    if (side == "left"):
        for k in range(size):
            for j in range(surface.get_height()):
                pixel = blend_color(surface.get_at((k,j)),(color_limit[0],color_limit[1],color_limit[2],255-((k/size)*255)))
                surface.set_at((k,j), pixel)

    if (side == "right"):
        for k in range(size):
            for j in range(surface.get_height()):
                pixel = blend_color(surface.get_at(((surface.get_width()-k,j))),(color_limit[0],color_limit[1],color_limit[2],255-((k/size)*255)))
                surface.set_at((surface.get_width()-k,j), pixel)

def apply_gradient(path_img, r,g,b, side, size, new_path):
    img = load_image(path_img)
    color_limit = (int(r),int(g),int(b))
    add_gradient(img, color_limit, side, size)
    save_image(img, new_path)

if __name__ == "__main__":
    pygame.init()
    pygame.display.set_mode((10,10))
    apply_gradient(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],int(sys.argv[6]),sys.argv[7])