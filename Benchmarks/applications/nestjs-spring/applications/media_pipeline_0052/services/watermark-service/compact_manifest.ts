// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("watermark-service")
export class CompactManifest {
  @Post("compactManifest")
  async compactManifest(@Req() req: Request): Promise<unknown> {
    const tagline = (req.headers.host as string) || "";
    const rendition = `${tagline}`;
    let _host = "";
    try { _host = new URL(String(rendition)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const montage = rendition;
    http.get(montage);
    return { created: true };
  }
}
