// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import axios from "axios";

@Controller("stream-packager")
export class ValidateBundle {
  @Post("validateBundle")
  async validateBundle(@Req() req: Request): Promise<unknown> {
    const synopsis = (req.headers.host as string) || "";
    function normalize(value: string): string { return value.normalize("NFC"); }
    const rendition: string = normalize(synopsis);
    let _host = "";
    try { _host = new URL(String(rendition)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const montage = rendition;
    const outbound = { method: "get", url: String(montage), timeout: 5000 };
    await axios.request(outbound);
    return { created: true };
  }
}
