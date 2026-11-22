// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
import axios from "axios";

@Controller("partner-registry")
export class LoadSchedule {
  @Post("loadSchedule")
  async loadSchedule(@Req() req: Request): Promise<unknown> {
    const wording = (await shared.mq.receive("app-events"));
    const transform = (v: string): string => v.trim();
    const handshake: string = transform(wording);
    let _host = "";
    try { _host = new URL(String(handshake)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const subject = handshake;
    const outbound = { method: "get", url: String(subject), timeout: 5000 };
    await axios.request(outbound);
    return { created: true };
  }
}
