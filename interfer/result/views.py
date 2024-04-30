from django.shortcuts import render
import numpy as np


import plotly.graph_objects as go

# Create your views here.
def good_solve(L):
	fig = go.Figure()

	lambda_0 = 632e-9 
	num_points = 100
	
	delta_L = np.linspace(0, L, num_points)
	I =  (1 + np.cos(2 * np.pi * delta_L / lambda_0))
	fig.add_trace(go.Scatter(x = delta_L,y=I, mode='lines+markers'))
	fig.update_layout(
		font = dict(size=15),
		height= 400,
		width = 700,
		template='simple_white',
		xaxis_title="Оптическая разность путей (м)",
		yaxis_title="Интенсивность",
		title = 'Интерференционные полосы интерферометра Майкельсона'
	)
	return fig

def start(request):
	L = 100
	if request.method == 'POST':
		L = int(request.POST.get("sholder"))
	
	fig = good_solve(L)
	plot_html = fig.to_html(full_html = False,include_plotlyjs='cdn')
	data={
		"graph":plot_html,
		"L":L,

	}
	return render(request, "index.html",data)