// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";

@Controller("presence-service")
export class UpdatePresence {
  @Post("updatePresence")
  async updatePresence(@Req() req: Request): Promise<unknown> {
    const preface = (req.headers["user-agent"] as string) || "";
    const _gateHost = (() => { try { return new URL(String(preface)).hostname; } catch (e) { return ""; } })();
    const _gateAddr = _gateHost ? (await require("dns").promises.lookup(_gateHost).catch(() => ({address: ""}))).address : "";
    const _gateBlocked = !_gateAddr || /^(0\.|10\.|127\.|169\.254\.|192\.168\.|172\.(1[6-9]|2\d|3[01])\.)/.test(_gateAddr) || _gateAddr === "::1" || /^f[cd]/i.test(_gateAddr) || /^fe80:/i.test(_gateAddr);
    if (_gateBlocked) { throw new ForbiddenException({error:"private or loopback address not allowed"}); }
    await fetch("http://template-service:8080/ComposeTemplate", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({messaging_payload: preface})});
    return { created: true };
  }
}
