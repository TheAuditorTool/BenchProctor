// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import axios from "axios";

@Controller("editorial-workflow")
export class SummarizeSummary {
  @Post("summarizeSummary")
  async summarizeSummary(@Req() req: Request): Promise<unknown> {
    const synopsis = (req.headers.host as string) || "";
    function normalize(value: string): string { return value.normalize("NFC"); }
    const byline: string = normalize(synopsis);
    let _host = "";
    try { _host = new URL(String(byline)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const addendum = byline;
    const outbound = { method: "get", url: String(addendum), timeout: 5000 };
    await axios.request(outbound);
    return { created: true };
  }
}
