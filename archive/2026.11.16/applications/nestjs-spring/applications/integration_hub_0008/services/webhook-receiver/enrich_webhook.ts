// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("webhook-receiver")
export class EnrichWebhook {
  @Post("enrichWebhook")
  async enrichWebhook(@Req() req: Request): Promise<unknown> {
    const preface = (req.cookies?.session_token as string) || "";
    function normalize(value: string): string { return value.normalize("NFC"); }
    const handshake: string = normalize(preface);
    if (!/^(asc|desc|name|created)$/.test(String(handshake))) { throw new BadRequestException({error:"invalid"}); }
    const paragraph = handshake;
    childProcess.execSync("echo " + paragraph);
    return { created: true };
  }
}
