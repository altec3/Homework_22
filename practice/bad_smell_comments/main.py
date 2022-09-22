class Unit:
    # ...
    def move(self, field, coord_x: int, coord_y: int, direction, fly: bool, crawl: bool, speed: int = 1):

        new_x = 0
        new_y = 0

        if fly and crawl:
            raise ValueError('Рожденный ползать летать не должен!')

        if fly:
            speed *= 1.2
            if direction == 'UP':
                new_y = coord_y + speed
                new_x = coord_x
            elif direction == 'DOWN':
                new_y = coord_y - speed
                new_x = coord_x
            elif direction == 'LEFT':
                new_y = coord_y
                new_x = coord_x - speed
            elif direction == 'RIGHT':
                new_y = coord_y
                new_x = coord_x + speed

            field.set_unit(x=new_x, y=new_y, unit=self)

        if crawl:
            speed *= 0.5
            if direction == 'UP':
                new_y = coord_y + speed
                new_x = coord_x
            elif direction == 'DOWN':
                new_y = coord_y - speed
                new_x = coord_x
            elif direction == 'LEFT':
                new_y = coord_y
                new_x = coord_x - speed
            elif direction == 'RIGHT':
                new_y = coord_y
                new_x = coord_x + speed

            field.set_unit(x=new_x, y=new_y, unit=self)
#     ...
