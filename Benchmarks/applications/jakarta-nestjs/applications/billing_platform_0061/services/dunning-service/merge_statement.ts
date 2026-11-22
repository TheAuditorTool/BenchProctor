// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;
import axios from "axios";

@Controller("dunning-service")
export class MergeStatement {
  @Post("mergeStatement")
  async mergeStatement(@Req() req: Request): Promise<unknown> {
    const footnote = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
    function normalize(value: string): string { return value.normalize("NFC"); }
    const remittance: string = normalize(footnote);
    let _host = "";
    try { _host = new URL(String(remittance)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const arrears = remittance;
    const outbound = { method: "get", url: String(arrears), timeout: 5000 };
    await axios.request(outbound);
    return { created: true };
  }
}
