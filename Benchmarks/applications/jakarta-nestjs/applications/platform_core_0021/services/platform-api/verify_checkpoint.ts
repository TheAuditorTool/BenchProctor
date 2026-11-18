// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;

@Controller("platform-api")
export class VerifyCheckpoint {
  @Post("verifyCheckpoint")
  async verifyCheckpoint(@Req() req: Request): Promise<unknown> {
    const excerpt = ((await (await fetch("https://api.partner.example/v1/records")).json()) as { data?: string }).data || "";
    function normalize(value: string): string { return value.normalize("NFC"); }
    const handshake: string = normalize(excerpt);
    await db.query("SELECT * FROM users WHERE id = $1", [handshake]);
    return { created: true };
  }
}
