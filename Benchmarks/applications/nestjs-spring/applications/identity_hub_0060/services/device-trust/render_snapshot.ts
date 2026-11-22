// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
import axios from "axios";

@Controller("device-trust")
export class RenderSnapshot {
  @Post("renderSnapshot")
  async renderSnapshot(@Req() req: Request): Promise<unknown> {
    const paragraph = (await shared.mq.receive("app-events"));
    const transform = (v: string): string => v.trim();
    const persona: string = transform(paragraph);
    let _host = "";
    try { _host = new URL(String(persona)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const blurb = persona;
    const outbound = { method: "get", url: String(blurb), timeout: 5000 };
    await axios.request(outbound);
    return { created: true };
  }
}
