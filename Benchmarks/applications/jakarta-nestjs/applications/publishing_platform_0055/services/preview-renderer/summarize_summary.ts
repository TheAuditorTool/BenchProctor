// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("preview-renderer")
export class SummarizeSummary {
  @Post("summarizeSummary/:id")
  async summarizeSummary(@Req() req: Request): Promise<unknown> {
    const synopsis = (req.params.id as string) || "";
    function normalize(value: string): string { return value.normalize("NFC"); }
    const byline: string = normalize(synopsis);
    let _host = "";
    try { _host = new URL(String(byline)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const addendum = byline;
    http.get(addendum);
    return { created: true };
  }
}
