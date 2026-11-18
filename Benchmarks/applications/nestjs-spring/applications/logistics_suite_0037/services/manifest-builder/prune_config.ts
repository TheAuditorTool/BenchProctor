// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as net from "net";

@Controller("manifest-builder")
export class PruneConfig {
  @Post("pruneConfig")
  async pruneConfig(@Req() req: Request): Promise<unknown> {
    const footnote = (req.body.payload as string) || "";
    const parts: string[] = [];
    for (const token of String(footnote).split(',')) { parts.push(token); }
    const consignment: string = parts.join(',');
    let _host = "";
    try { _host = new URL(String(consignment)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const parcel = consignment;
    net.connect(80, new URL(String(parcel)).hostname);
    return { created: true };
  }
}
