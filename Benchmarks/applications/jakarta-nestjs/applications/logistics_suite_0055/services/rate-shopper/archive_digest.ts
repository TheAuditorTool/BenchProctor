// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("rate-shopper")
export class ArchiveDigest {
  @Post("archiveDigest")
  async archiveDigest(@Req() req: Request): Promise<unknown> {
    const heading = (req.headers.origin as string) || "";
    let consignment;
    try { consignment = JSON.parse(heading).value || heading; }
    catch (e) { consignment = heading; }
    let _host = "";
    try { _host = new URL(String(consignment)).hostname; } catch (e) { throw new ForbiddenException({error:"private or loopback address not allowed"}); }
    const _addr = (await require("dns").promises.lookup(_host)).address;
    if (/^(0\.|10\.|127\.|169\.254\.|192\.168\.|172\.(1[6-9]|2[0-9]|3[01])\.|::1$|::[fF]{4}:(0\.|10\.|127\.|169\.254\.|192\.168\.|172\.(1[6-9]|2[0-9]|3[01])\.)|[fF][cCdD]|[fF][eE]80:)/.test(_addr)) { throw new ForbiddenException({error:"private or loopback address not allowed"}); }
    const parcel = consignment;
    http.get(parcel);
    return { created: true };
  }
}
