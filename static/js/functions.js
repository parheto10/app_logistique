function edit(url){
    event.preventDefault();
    var csrfToken = $('[name="csrfmiddlewaretoken"]').val();
    $.ajax({
        url: url,
        method: "GET",
        dataType : "json",
        success:function(response){
           $('#Modal').html(response.templateStr)
           $('#Modal').modal('show')
           
        }
    });
}

function termine_cours(url) {
    event.preventDefault();
        swal({
				title: "Voulez vous vraiment terminer cette course ?",
				icon: "warning",
				buttons: true,
				dangerMode: true,
			})
				.then((willDelete) => {
				if (willDelete) {
					$.get(url , { });
					swal("course terminer avec succès", {
						icon: "success",
					})
                    .then((ok) => {
                        if(ok) {
                            location.reload();
                        }
                    });
                    
				} else {

		}
		});

}
function termine_mission(url) {
    event.preventDefault();
        swal({
				title: "Voulez vous vraiment terminer cette Mission ?",
				icon: "warning",
				buttons: true,
				dangerMode: true,
			})
				.then((willDelete) => {
				if (willDelete) {
					$.get(url , { });
					swal("Mission terminer avec succès", {
						icon: "success",
					})
                    .then((ok) => {
                        if(ok) {
                            location.reload();
                        }
                    });
                    
				} else {

		}
		});

}

function MoyenOfChange(){
    var moyen = $("#moyen").val().trim();

    if(moyen == "OUI"){
        $("#louer").css('display', 'none');
        $("#service").css('display', 'block');
    }else if(moyen == "NON"){
        $("#service").css('display', 'none');
        $("#louer").css('display', 'block');
    }else{
        $("#service").css('display', 'none');
        $("#louer").css('display', 'none'); 
    }
    
}

function restitution(url) {
    event.preventDefault();
        swal({
				title: "Voulez vous remettre cet matériel ?",
				icon: "info",
				buttons: true,
				dangerMode: true,
			})
				.then((willDelete) => {
				if (willDelete) {
					$.get(url , { });
					swal("Restitution effectué avec succès !", {
						icon: "success",
					})
                    .then((ok) => {
                        if(ok) {
                            location.reload();
                        }
                    });
                    
				} else {

		}
		});

}


