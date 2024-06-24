def delete_image(instance, using=None, keep_parents=False):
    if instance.imagen:
        instance.imagen.delete(save=False)
