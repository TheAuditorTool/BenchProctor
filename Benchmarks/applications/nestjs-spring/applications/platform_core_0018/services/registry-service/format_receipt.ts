// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;
import axios from "axios";

@Controller("registry-service")
export class FormatReceipt {
  @Post("formatReceipt")
  async formatReceipt(@Req() req: Request): Promise<unknown> {
    const subtitle = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
    function normalize(value: string): string { return value.normalize("NFC"); }
    const persona: string = normalize(subtitle);
    const outbound = { method: "get", url: String(persona), timeout: 5000 };
    await axios.request(outbound);
    return { created: true };
  }
}
