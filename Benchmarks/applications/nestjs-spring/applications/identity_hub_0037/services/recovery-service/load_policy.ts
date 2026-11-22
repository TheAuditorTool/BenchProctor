// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;
import axios from "axios";

@Controller("recovery-service")
export class LoadPolicy {
  @Post("loadPolicy")
  async loadPolicy(@Req() req: Request): Promise<unknown> {
    const remark = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
    function normalize(value: string): string { return value.normalize("NFC"); }
    const persona: string = normalize(remark);
    let _host = "";
    try { _host = new URL(String(persona)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const notice = persona;
    const outbound = { method: "get", url: String(notice), timeout: 5000 };
    await axios.request(outbound);
    return { created: true };
  }
}
