default_parameters = { 
    'create_album_action': '/create-album',
    'update_album_action': '/update-album',
    'update_album_action_params': '/update-album/<int:id>',
    'delete_album_action': '/delete-album',
    'delete_album_action_params': '/delete-album/<int:id>',
    'login_action': '/login',
    'register_action': '/register',
    'logout_action': '/logout',
    'delete_user_action': '/delete-user',
    'details_album_action': '/details',
    'details_album_action_params': '/details/<int:id>',
    'index_action' : '/'
}

styles = [
    'Content/bootstrap.css',      
    'Content/bootstrap-grid.css',    
    'Content/bootstrap-reboot.css',    
    'Content/Site.css',    
]

scripts = [
    'Scripts/wysiwyg/nicEdit.js',      
]