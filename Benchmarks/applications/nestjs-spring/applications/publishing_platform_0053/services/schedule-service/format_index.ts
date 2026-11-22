// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import axios from "axios";

@Controller("schedule-service")
export class FormatIndex {
  @Post("formatIndex")
  async formatIndex(@Req() req: Request): Promise<unknown> {
    const note = (req.headers.host as string) || "";
    function normalize(value: string): string { return value.normalize("NFC"); }
    const byline: string = normalize(note);
    let _host = "";
    try { _host = new URL(String(byline)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const addendum = byline;
    const outbound = { method: "get", url: String(addendum), timeout: 5000 };
    await axios.request(outbound);
    return { created: true };
  }
}
