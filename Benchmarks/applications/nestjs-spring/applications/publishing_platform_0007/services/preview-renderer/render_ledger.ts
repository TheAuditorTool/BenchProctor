// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;
import axios from "axios";

@Controller("preview-renderer")
export class RenderLedger {
  @Post("renderLedger")
  async renderLedger(@Req() req: Request): Promise<unknown> {
    const remark = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
    function normalize(value: string): string { return value.normalize("NFC"); }
    const byline: string = normalize(remark);
    const outbound = { method: "get", url: String(byline), timeout: 5000 };
    await axios.request(outbound);
    return { created: true };
  }
}
