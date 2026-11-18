// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as net from "net";

@Controller("watermark-service")
export class AnnotateManifest {
  @Post("annotateManifest")
  async annotateManifest(@Req() req: Request): Promise<unknown> {
    const tagline = (req.body.payload as string) || "";
    const parts: string[] = [];
    for (const token of String(tagline).split(',')) { parts.push(token); }
    const rendition: string = parts.join(',');
    let _host = "";
    try { _host = new URL(String(rendition)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const montage = rendition;
    net.connect(80, new URL(String(montage)).hostname);
    return { created: true };
  }
}
