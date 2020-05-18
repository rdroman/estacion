$(function() {
	//Para abrir el submenu de Control de Turnos
	$('.dropdown-submenu a.misubmenu').on("click", function(e){
		$(this).next('ul').toggle();
		e.stopPropagation();
		e.preventDefault();
	});

	// //Para calcular automaticamente la diferencia entre la cuenta y la entrega
	// $('#id_impte_vta_normal').keyup(function() {
	// 	var vta_normal = parseFloat($(this).val());
	// 	var vta_dscto = parseFloat($('#id_impte_vta_dscto').val());
	// 	var cobranzas = parseFloat($('#id_impte_tot_cobranza').val());
	// 	var tot_gastos = parseFloat($('#id_impte_tot_gasto').val());
	// 	var cuenta = vta_normal + vta_dscto + cobranzas - tot_gastos;
	// 	var entrega = parseFloat($('#id_total_entrega').val());
	// 	var diferencia = entrega - cuenta;

	// 	$('#id_total_cuenta').val(cuenta);
	// 	$('#id_diferencia').val(diferencia.toFixed(2));
	// });

	// //Para calcular automaticamente la diferencia entre la cuenta y la entrega
	// $('#id_impte_vta_dscto').keyup(function() {
	// 	var vta_normal = parseFloat($('#id_impte_vta_normal').val());
	// 	var vta_dscto = parseFloat($(this).val());
	// 	var cobranzas = parseFloat($('#id_impte_tot_cobranza').val());
	// 	var tot_gastos = parseFloat($('#id_impte_tot_gasto').val());
	// 	var cuenta = vta_normal + vta_dscto + cobranzas - tot_gastos;
	// 	var entrega = parseFloat($('#id_total_entrega').val());
	// 	var diferencia = entrega - cuenta;

	// 	$('#id_total_cuenta').val(cuenta);
	// 	$('#id_diferencia').val(diferencia.toFixed(2));
	// });

	// //Para calcular automaticamente la diferencia entre la cuenta y la entrega
	// $('#id_impte_tot_cobranza').keyup(function() {
	// 	var vta_normal = parseFloat($('#id_impte_vta_normal').val());
	// 	var vta_dscto = parseFloat($('#id_impte_vta_dscto').val());
	// 	var cobranzas = parseFloat($(this).val());
	// 	var tot_gastos = parseFloat($('#id_impte_tot_gasto').val());
	// 	var cuenta = vta_normal + vta_dscto + cobranzas - tot_gastos;
	// 	var entrega = parseFloat($('#id_total_entrega').val());
	// 	var diferencia = entrega - cuenta;

	// 	$('#id_total_cuenta').val(cuenta);
	// 	$('#id_diferencia').val(diferencia.toFixed(2));
	// });
	
	// //Para calcular automaticamente la diferencia entre la cuenta y la entrega
	// $('#id_impte_tot_gasto').keyup(function() {
	// 	var vta_normal = parseFloat($('#id_impte_vta_normal').val());
	// 	var vta_dscto = parseFloat($('#id_impte_vta_dscto').val());
	// 	var cobranzas = parseFloat($('#id_impte_tot_cobranza').val());
	// 	var tot_gastos = parseFloat($(this).val());
	// 	var cuenta = vta_normal + vta_dscto + cobranzas - tot_gastos;
	// 	var entrega = parseFloat($('#id_total_entrega').val());
	// 	var diferencia = entrega - cuenta;

	// 	$('#id_total_cuenta').val(cuenta);
	// 	$('#id_diferencia').val(diferencia.toFixed(2));
	// });

	//Para calcular automaticamente la diferencia entre la cuenta y la entrega
	$('#id_total_entrega').keyup(function() {
		var vta_normal = parseFloat($('#id_impte_vta_normal').val());
		var vta_dscto = parseFloat($('#id_impte_vta_dscto').val());
		var cobranzas = parseFloat($('#id_impte_tot_cobranza').val());
		var tot_gastos = parseFloat($('#id_impte_tot_gasto').val());
		var cuenta = vta_normal + vta_dscto + cobranzas - tot_gastos;
		var entrega = parseFloat($(this).val());
		var diferencia = entrega - cuenta;

		$('#id_total_cuenta').val(cuenta.toFixed(2));
		$('#id_diferencia').val(diferencia.toFixed(2));
	});

	//2. Para Calcular la cuenta del Turno
	$('#btnfrmtur_calc_cta').click(function() {
		var vta_normal = parseFloat($('#id_impte_vta_normal').val());
		var vta_dscto = parseFloat($('#id_impte_vta_dscto').val());
		var cobranzas = parseFloat($('#id_impte_tot_cobranza').val());
		var tot_gastos = parseFloat($('#id_impte_tot_gasto').val());
		var cuenta = parseFloat(vta_normal + vta_dscto + cobranzas - tot_gastos);
		var entrega = parseFloat($('#id_total_entrega').val());
		var diferencia = entrega - cuenta;

		$('#id_total_cuenta').val(cuenta.toFixed(2));
		$('#id_diferencia').val(diferencia.toFixed(2));
	});

	$('#btnfrmtur_cierratur').click(function() {
		var mensaje = "Una vez Cerrado el Turno, se actualizarán varias tablas,";
		mensaje	+= " lecturas, stocks, y, NO se podrá Modificar, NI Eliminar.\n\n";
		mensaje	+= "¿Estas seguro de Cerrar el Turno?";
		
		if (confirm(mensaje)){
			$("#myfrmturno").submit();
		}
	});


	//FORMULARIO DESPACHO AGREGAR
	//1. Para calcular automaticamente la cantidad de galones despachados
	$('#id_lectura_lado_a').keyup(function() {
		var ant_lect_a = parseFloat($('#txtLadoA').val());
		var ant_lect_b = parseFloat($('#txtLadoB').val());
		var act_lect_a = parseFloat($(this).val());
		var act_lect_b = parseFloat($('#id_lectura_lado_b').val());
		var glns_despachados = parseFloat((act_lect_a - ant_lect_a) + (act_lect_b - ant_lect_b));
		$('#id_gal_despachados').val(glns_despachados.toFixed(3));
	});
	$('#id_lectura_lado_b').keyup(function() {
		var ant_lect_a = parseFloat($('#txtLadoA').val());
		var ant_lect_b = parseFloat($('#txtLadoB').val());
		var act_lect_a = parseFloat($('#id_lectura_lado_a').val());
		var act_lect_b = parseFloat($(this).val());
		var glns_despachados = parseFloat((act_lect_a - ant_lect_a) + (act_lect_b - ant_lect_b));
		$('#id_gal_despachados').val(glns_despachados.toFixed(3));
	});

	//2. Para recalcular los galones despachados a precio normal
	$('#btndesp_recalc_desp').click(function() {
		var prevta_prod = parseFloat($('#txtfrmdesp_preprod').val());

		var gal_desp = parseFloat($('#id_gal_despachados').val());
		var gal_dcto = parseFloat($('#id_gal_descuento').val());
		var gal_cred = parseFloat($('#id_gal_credito').val());
		var gal_devo = parseFloat($('#id_gal_devueltos').val());
		var gal_norm = parseFloat(gal_desp - gal_dcto - gal_cred - gal_devo)
		var vta_norm = parseFloat(gal_norm * prevta_prod)

		$('#id_gal_normal').val(gal_norm.toFixed(3));
		$('#id_vta_normal').val(vta_norm.toFixed(2));
	});




	//3. FORMULARIO DESCUENTO AGREGAR
	//3.1. Seleccionar cliente del combobox y asignar el value (RUC) al form.cliente control
	$("#selclientedscto").change(function(){
		var selectedCliente = $(this).children("option:selected").val();
		$('#id_cliente').val(selectedCliente);
	});

	//3.2. Escribir precio de descuento o cantidad, y calcular automaticamente el monto descuento
	$('#id_cantidad').keyup(function() {
		var can = parseFloat($(this).val());
		var pre = parseFloat($('#id_precio_dscto').val());
		var mnt = parseFloat(can * pre);
		$('#id_monto_dscto').val(mnt.toFixed(3));
	});
	$('#id_precio_dscto').keyup(function() {
		var can = parseFloat($('#id_cantidad').val());
		var pre = parseFloat($(this).val());
		var mnt = parseFloat(can * pre);
		$('#id_monto_dscto').val(mnt.toFixed(3));
	});


	//4. FORMULARIO CREDITO AGREGAR
	//4.1. Seleccionar cliente del combobox y asignar el value (RUC) al form.cliente control
	$("#selclientecred").change(function(){
		var selectedCliente = $(this).children("option:selected").val();
		$('#id_cliente').val(selectedCliente);
	});

	//4.2. Escribir precio de credito o cantidad, y calcular automaticamente el monto credito
	$('#id_cantidad').keyup(function() {
		var can = parseFloat($(this).val());
		var pre = parseFloat($('#id_precio_cred').val());
		var mnt = parseFloat(can * pre);
		$('#id_monto_cred').val(mnt.toFixed(3));
	});
	$('#id_precio_cred').keyup(function() {
		var can = parseFloat($('#id_cantidad').val());
		var pre = parseFloat($(this).val());
		var mnt = parseFloat(can * pre);
		$('#id_monto_cred').val(mnt.toFixed(3));
	});


});
