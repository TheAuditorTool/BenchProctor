// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
import axios from "axios";

@Controller("signature-verifier")
export class FetchPolicy {
  @Post("fetchPolicy")
  async fetchPolicy(@Req() req: Request): Promise<unknown> {
    const summary = (await shared.mq.receive("app-events"));
    const transform = (v: string): string => v.trim();
    const handshake: string = transform(summary);
    let _host = "";
    try { _host = new URL(String(handshake)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const paragraph = handshake;
    const outbound = { method: "get", url: String(paragraph), timeout: 5000 };
    await axios.request(outbound);
    return { created: true };
  }
}
