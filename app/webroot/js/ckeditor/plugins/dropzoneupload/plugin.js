CKEDITOR.plugins.add( 'dropzoneupload', {
    // requires: 'filetools',
    // beforeInit: function( editor ) {
    //     if (!!!CKEDITOR.fileTools) {
    //         console.log("Please add the plugins fileTools and its requirements.")
    //     }
    // },
    init: function( editor ) {
        // var fileDialog = $('<input type="file">');
        
        // fileDialog.on('change', function (e) {
        //     var fileTools = CKEDITOR.fileTools,
        //         uploadUrl = fileTools.getUploadUrl( editor.config, 'image' ),
        //         file = e.target.files[0],
        //         loader = editor.uploadRepository.create(file),
        //         reader = new FileReader(),
        //         notification,
        //         img;
            
        //     // verify
        //     if (!/image/i.test(file.type)) {
        //         notification = editor.showNotification( 'Please check the correct format.', 'warning' );

        //         setTimeout(function() {
        //             notification.hide()
        //         }, 2000);

        //         return false
        //     }
            
        //     loader.upload(uploadUrl);

        //     // preview image
        //     reader.readAsDataURL(e.target.files[0]);

        //     reader.onload = function (e) {
        //         img = editor.document.createElement('img');
        //         img.setAttribute('src', e.target.result);
        //         img.setStyle('opacity', 0.3);
        //         editor.insertElement(img);
        //     }

        //     loader.on('uploaded', function(evt) {
        //         editor.widgets.initOn(img, 'image', {
        //             src: evt.sender.url
        //         });
        //         img.setAttribute('src', evt.sender.url);
        //         img.setStyle('opacity', 1);
        //     });

        //     loader.on('error', function() {
        //         img.remove()
        //     });

        //     fileTools.bindNotifications(editor, loader);
            
        //     // empty input
        //     fileDialog[0].value = "";
        // });

        editor.ui.addButton( 'MultiUpload', {
            label: 'Upload Nhiều files',
            command: 'openDialog',
            toolbar: 'insert',
            icon: this.path + 'icon.png', 
        });

        editor.addCommand('openDialog', {
            exec: function(editor) {
                // fileDialog.click();
                dropzone_action = 'insert_ckeditor';
               $('#modal-dropzone').modal();


                // var parentWindow = ( window.parent == window ) ? window.opener : window.parent;
                // for(var instanceName in CKEDITOR.instances) {
                //   current_edior_id = CKEDITOR.instances[instanceName].name;
                //   break;
                // }
                current_edior_id = editor.name;

                console.log('plugin dropzone -->  editor.name: ' + editor.name);
                // console.log('current_edior_id: ' + current_edior_id);
            }
        });
    }
});
