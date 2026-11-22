// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
import axios from "axios";

@Controller("digest-service")
export class ArchiveConfig {
  @Post("archiveConfig")
  async archiveConfig(@Req() req: Request): Promise<unknown> {
    const footnote = (await shared.mq.receive("app-events"));
    const transform = (v: string): string => v.trim();
    const bulletin: string = transform(footnote);
    let _host = "";
    try { _host = new URL(String(bulletin)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const snippet = bulletin;
    const outbound = { method: "get", url: String(snippet), timeout: 5000 };
    await axios.request(outbound);
    return { created: true };
  }
}
