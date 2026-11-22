// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import axios from "axios";

@Controller("revision-store")
export class ResolveHeader {
  @Post("resolveHeader")
  async resolveHeader(@Req() req: Request): Promise<unknown> {
    const transcript = (req.headers.host as string) || "";
    function normalize(value: string): string { return value.normalize("NFC"); }
    const addendum: string = normalize(transcript);
    let _host = "";
    try { _host = new URL(String(addendum)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const byline = addendum;
    const outbound = { method: "get", url: String(byline), timeout: 5000 };
    await axios.request(outbound);
    return { created: true };
  }
}
