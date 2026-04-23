import { get_conn } from "@/lib/db";

export async function GET() {

  const conn = await get_conn();

  const result = await conn.query(
    "SELECT * FROM jobs ORDER BY id DESC LIMIT 100"
  );

  return Response.json(result.rows);
}
