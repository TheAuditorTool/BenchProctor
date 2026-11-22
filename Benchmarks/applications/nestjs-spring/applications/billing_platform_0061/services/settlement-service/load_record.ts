// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;
import axios from "axios";

@Controller("settlement-service")
export class LoadRecord {
  @Post("loadRecord")
  async loadRecord(@Req() req: Request): Promise<unknown> {
    const footnote = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
    function normalize(value: string): string { return value.normalize("NFC"); }
    const remittance: string = normalize(footnote);
    const outbound = { method: "get", url: String(remittance), timeout: 5000 };
    await axios.request(outbound);
    return { created: true };
  }
}
