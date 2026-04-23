import { get_conn } from "@/lib/db";

export async function GET() {
  try {
    const conn = await get_conn();

    const result = await conn.query(
      "SELECT cpu, gpu, success FROM boot_logs ORDER BY created_at DESC LIMIT 100"
    );

    return Response.json({
      success: true,
      data: result.rows
    });

  } catch (error: any) {

    return Response.json({
      success: false,
      error: error.message
    }, { status: 500 });

  }
}
