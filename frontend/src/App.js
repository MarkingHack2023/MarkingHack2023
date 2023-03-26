import React, { useEffect, useState } from 'react';
import axios from 'axios'
import { AreaChart, Area, LineChart, Line, BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend } from 'recharts';
import Select from 'react-select'
import { Table } from 'react-bootstrap'

const productsOptions = [{ value: 'C6AD4B84092CCBB3E3729F73B00C55A1', label: 'Product C6AD'}];
const regionsOptions = [{ value: '50', label: 'MO'}, { value: '77', label: 'Moscow'}];
const postCodesOptions = [{ value: '141031', label: '141031'}];

function MyComponent() {
    const [product, setProduct] = useState(null);
    const [region, setRegion] = useState(null);
    const [postCode, setPostCode] = useState(null);

    const handleProductChange = (selectedOption) => {
        setProduct(selectedOption);
    }

    const handleRegionChange = (selectedOption) => {
        setRegion(selectedOption);
    }

    const handlePostCodeChange = (selectedOption) => {
        setPostCode(selectedOption);
    }

    const handleSubmit = () => {
        const filters = {
            product_short_name: product.value,
            region_code: region.value,
            postal_code: postCode.value,
            time_horizon: 'Последний год'
        };

        axios.post('/api/data', filters)
            .then(response => {
            // обработка ответа от backend
            })
            .catch(error => {
                console.error(error);
            });
    }

    return (
    <div>
        <h2>Фильтры</h2>
        <div>
            <Select
                options={productsOptions}
                value={product}
                onChange={handleProductChange}
            />
            <Select
                options={regionsOptions}
                value={region}
                onChange={handleRegionChange}
            />
            <Select
                options={postCodesOptions}
                value={postCode}
                onChange={handlePostCodeChange}
            />
        <button onClick={handleSubmit}>Применить фильтры</button>
        </div>
    </div>
    );
}

function App() {
  const [getMessage, setGetMessage] = useState({ message: [], status: null });

  useEffect(() => {
    axios.get('http://85.93.40.83:5000/api/function').then(response => {
      console.log("SUCCESS", response);
//      setGetMessage({ message: response.data, status: response.status })
        setGetMessage(response.data);
    }).catch(error => {
      console.log(error);
    });
  }, []);

  return (
    <div>
    <div>
	<h1>Добрый ЗНАК / Остатки товара по регионам</h1>
    </div>
    <div class="container">
    <div class="box-filter">
    <MyComponent />
    </div>
    <div class="box-graph" style={{ position: 'relative' }}>
    <AreaChart width={730} height={350} data={getMessage.message} style={{ position: 'absolute', top: 0, left: 0 }}
	margin={{ top: 10, right: 30, left: 0, bottom: 0 }}>
	<defs>
	    <linearGradient id="colorGreen" x1="0" y1="0" x2="0" y2="1">
		<stop offset="5%" stopColor="#4daf4a" stopOpacity={0.8}/>
		<stop offset="95%" stopColor="#4daf4a" stopOpacity={0}/>
	    </linearGradient>
	    <linearGradient id="colorYellow" x1="0" y1="0" x2="0" y2="1">
		<stop offset="5%" stopColor="#fdc086" stopOpacity={0.8}/>
		<stop offset="95%" stopColor="#fdc086" stopOpacity={0}/>
	    </linearGradient>
	    <linearGradient id="colorRed" x1="0" y1="0" x2="0" y2="1">
		<stop offset="5%" stopColor="#e41a1c" stopOpacity={0.8}/>
		<stop offset="95%" stopColor="#e41a1c" stopOpacity={0}/>
	    </linearGradient>
	</defs>
        <CartesianGrid strokeDasharray="3 3" />
        <XAxis dataKey="date" domain={['2022-01-01', '2022-02-01']} />
        <YAxis domain={['auto', 'auto']} />
        <Tooltip />
        <Legend />
        <Area type="monotone" dataKey="green_estimate" stroke="#4daf4a" fillOpacity={1} fill="url(#colorGreen)" />
        <Area type="monotone" dataKey="yellow_estimate" stroke="#fdc086" fillOpacity={1} fill="url(#colorYellow)" />
        <Area type="monotone" dataKey="red_estimate" stroke="#e41a1c" fillOpacity={1} fill="url(#colorRed)" />
        <Area type="monotone" dataKey="stock" stroke="#000000" fillOpacity={0} dot={{ stroke: '#000000', strokeWidth: 2 }} />
    </AreaChart>
    </div>
    <div class="box-table">
    <Table class="table" id="description">
     <thead>
      <tr>
	<th>Дата</th>
	<th>Текущий остаток</th>
	<th>Достаточно</th>
	<th>Недостаток</th>
	<th>Дефицит</th>
      </tr>
     </thead>
    <tbody>
	{getMessage.message.map(item => (
	    <tr>
	     <td>{item.date}</td>
	     <td>{item.stock}</td>
	     <td>{item.green_estimate}</td>
	     <td>{item.yellow_estimate}</td>
	     <td>{item.red_estimate}</td>
	    </tr>
	))}
    </tbody>
    </Table>
    </div>
    </div>
    </div>
  );
}

export default App;