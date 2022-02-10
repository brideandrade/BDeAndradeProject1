
import arcade

def main():
    arcade.open_window(1000, 1000, "This is a drawing of a beach scenery")
    arcade.set_background_color(arcade.color.FRENCH_SKY_BLUE)
    water = arcade.create_rectangle(500, 400, 1000, 500, arcade.color.BABY_BLUE_EYES)
    sand1 = arcade.create_rectangle(500, 50, 1000, 500, arcade.color.KHAKI)
    sun1 = arcade.create_ellipse(1000, 1000, 450, 450, arcade.color.YELLOW)
    sand2 = arcade.create_ellipse(150, 250, 300, 200, arcade.color.KHAKI)
    sand3 = arcade.create_ellipse(400, 250, 300, 200, arcade.color.KHAKI)
    sand4 = arcade.create_ellipse(650, 250, 300, 200, arcade.color.KHAKI)
    sand5 = arcade.create_ellipse(900, 250, 300, 200, arcade.color.KHAKI)
    sunline1 = arcade.create_line(750, 750, 1000, 1000, arcade.color.YELLOW)
    sunline2 = arcade.create_line(850, 700, 1000, 1000, arcade.color.YELLOW)
    sunline3 = arcade.create_line(950, 675, 1000, 1000, arcade.color.YELLOW)
    sunline4 = arcade.create_line(700, 850, 1000, 1000, arcade.color.YELLOW)
    sunline5 = arcade.create_line(675, 950, 1000, 1000, arcade.color.YELLOW)

    arcade.start_render()
    water.draw()
    sand1.draw()
    sun1.draw()
    sand2.draw()
    sand3.draw()
    sand4.draw()
    sand5.draw()
    sunline1.draw()
    sunline2.draw()
    sunline3.draw()
    sunline4.draw()
    sunline5.draw()

    arcade.finish_render()
    arcade.run()


main()