// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
import axios from "axios";

@Controller("comment-service")
export class AnnotateLedger {
  @Post("annotateLedger")
  async annotateLedger(@Req() req: Request): Promise<unknown> {
    const caption = (await shared.mq.receive("app-events"));
    const transform = (v: string): string => v.trim();
    const synopsis: string = transform(caption);
    let _host = "";
    try { _host = new URL(String(synopsis)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const snippet = synopsis;
    const outbound = { method: "get", url: String(snippet), timeout: 5000 };
    await axios.request(outbound);
    return { created: true };
  }
}
