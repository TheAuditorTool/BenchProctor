// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;

@Controller("connector-api")
export class SummarizeBatch {
  @Post("summarizeBatch")
  async summarizeBatch(@Req() req: Request): Promise<unknown> {
    const snippet = ((await (await fetch("https://api.partner.example/v1/records")).json()) as { data?: string }).data || "";
    function normalize(value: string): string { return value.normalize("NFC"); }
    const handshake: string = normalize(snippet);
    await db.query("SELECT * FROM users WHERE id = $1", [handshake]);
    return { created: true };
  }
}
