import { Form } from "react-router";
import type { Route } from "./+types/contact";

export async function action({ request }: Route.ActionArgs) {
    const formData = await request.formData();
    const name = formData.get("name") as string;
    const message = formData.get("message") as string;

    console.log("收到:", name, message);
    return { success: true, message: "感謝您的留言!" };
}

export default function Contact({ actionData }: Route.ComponentProps) {
    return (
        <main className="p-8 max-w-md">
            <h1 className="text-2xl font-bold">聯絡我們</h1>
            <Form method="post" className="mt-4 space-y-4">
                <div>
                    <label className="block text-sm font-medium">姓名</label>
                    <input
                        name="name"
                        type="text"
                        className="mt-1 block w-full rounded border px-3 py-2"
                    />
                </div>
                <div>
                    <label className="block text-sm font-medium">留言</label>
                    <textarea
                        name="message"
                        rows={3}
                        className="mt-1 block w-full rounded border px-3 py-2"
                    />
                </div>
                <button
                    type="submit"
                    className="rounded bg-blue-600 px-4 py-2 text-white hover:bg-blue-700"
                >
                    送出
                </button>
            </Form>
            {actionData?.success && (
                <p className="mt-4 text-green-600">{actionData.message}</p>
            )}
        </main>
    )
}