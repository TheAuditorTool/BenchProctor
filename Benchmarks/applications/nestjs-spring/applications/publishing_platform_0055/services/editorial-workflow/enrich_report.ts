// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
import axios from "axios";

@Controller("editorial-workflow")
export class EnrichReport {
  @Post("enrichReport")
  async enrichReport(@Req() req: Request): Promise<unknown> {
    const synopsis = (await shared.mq.receive("app-events"));
    const transform = (v: string): string => v.trim();
    const byline: string = transform(synopsis);
    let _host = "";
    try { _host = new URL(String(byline)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const addendum = byline;
    const outbound = { method: "get", url: String(addendum), timeout: 5000 };
    await axios.request(outbound);
    return { created: true };
  }
}
