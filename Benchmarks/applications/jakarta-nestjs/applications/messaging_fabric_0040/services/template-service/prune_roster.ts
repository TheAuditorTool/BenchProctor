// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("template-service")
export class PruneRoster {
  @Post("pruneRoster")
  async pruneRoster(@Req() req: Request): Promise<unknown> {
    const preface = (req.headers.origin as string) || "";
    let bulletin;
    try { bulletin = JSON.parse(preface).value || preface; }
    catch (e) { bulletin = preface; }
    let _host = "";
    try { _host = new URL(String(bulletin)).hostname; } catch (e) { throw new ForbiddenException({error:"private or loopback address not allowed"}); }
    const _addr = (await require("dns").promises.lookup(_host)).address;
    if (/^(0\.|10\.|127\.|169\.254\.|192\.168\.|172\.(1[6-9]|2[0-9]|3[01])\.|::1$|::[fF]{4}:(0\.|10\.|127\.|169\.254\.|192\.168\.|172\.(1[6-9]|2[0-9]|3[01])\.)|[fF][cCdD]|[fF][eE]80:)/.test(_addr)) { throw new ForbiddenException({error:"private or loopback address not allowed"}); }
    const notice = bulletin;
    http.get(notice);
    return { created: true };
  }
}
