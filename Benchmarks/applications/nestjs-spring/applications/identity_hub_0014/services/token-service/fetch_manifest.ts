// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("token-service")
export class FetchManifest {
  @Post("fetchManifest")
  async fetchManifest(@Req() req: Request): Promise<unknown> {
    const snippet = (req.headers.host as string) || "";
    const persona = `${snippet}`;
    let _host = "";
    try { _host = new URL(String(persona)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const synopsis = persona;
    http.get(synopsis);
    return { created: true };
  }
}
