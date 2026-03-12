import type {Route} from "./+types/products"

export async function loader(){
    const products = [
        {id: 1, name: "商品 A", price:100},
        {id: 2, name: "商品 B", price:200},
    ];
    return {products};
}

export default function Products({loaderData}: Route.ComponentProps){
    return(
        <main className="p-8">
            <h1 className="text-2xl font-bold">商品列表</h1>
            <ul className="mt-4 space-y-2">
                {loaderData.products.map((p)=>(
                        <li key={p.id}>
                        {p.name} - ${p.price}
                    </li>
                ))}
            </ul>
        </main>
    );
}
