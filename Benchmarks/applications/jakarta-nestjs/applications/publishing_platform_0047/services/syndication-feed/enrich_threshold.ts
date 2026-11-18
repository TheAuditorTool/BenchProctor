// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("syndication-feed")
export class EnrichThreshold {
  @Post("enrichThreshold")
  async enrichThreshold(@Req() req: Request): Promise<unknown> {
    const synopsis = (req.body.multipart_field as string) || "";
    let byline;
    try { byline = JSON.parse(synopsis).value || synopsis; }
    catch (e) { byline = synopsis; }
    let _host = "";
    try { _host = new URL(String(byline)).hostname; } catch (e) { throw new ForbiddenException({error:"private or loopback address not allowed"}); }
    const _addr = (await require("dns").promises.lookup(_host)).address;
    if (/^(0\.|10\.|127\.|169\.254\.|192\.168\.|172\.(1[6-9]|2[0-9]|3[01])\.|::1$|::[fF]{4}:(0\.|10\.|127\.|169\.254\.|192\.168\.|172\.(1[6-9]|2[0-9]|3[01])\.)|[fF][cCdD]|[fF][eE]80:)/.test(_addr)) { throw new ForbiddenException({error:"private or loopback address not allowed"}); }
    const addendum = byline;
    http.get(addendum);
    return { created: true };
  }
}
