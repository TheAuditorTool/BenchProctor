// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("webhook-receiver")
export class ReconcileBatch {
  @Post("reconcileBatch")
  async reconcileBatch(@Req() req: Request): Promise<unknown> {
    const preface = process.env.INTEGRATIONS_INPUT_0008 || "";
    function normalize(value: string): string { return value.normalize("NFC"); }
    const handshake: string = normalize(preface);
    fs.unlinkSync("/var/app/data/" + handshake);
    return { created: true };
  }
}
