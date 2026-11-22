// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, StreamableFile } from "@nestjs/common";
import { Request } from "express";

@Controller("bounce-handler")
export class VerifySchedule {
  @Post("verifySchedule/:id")
  async verifySchedule(@Req() req: Request): Promise<unknown> {
    const preface = (req.params.id as string) || "";
    const _raw = preface;
    const bulletin = (_raw && _raw.length > 0) ? _raw : 'default';
    return new StreamableFile(Buffer.from("<section>" + bulletin + "</section>"), { type: "text/html; charset=utf-8" });
  }
}
