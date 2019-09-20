from mptt.admin import DraggableMPTTAdmin

class FileAdmin(DraggableMPTTAdmin):
    mptt_indent_field = 'name'