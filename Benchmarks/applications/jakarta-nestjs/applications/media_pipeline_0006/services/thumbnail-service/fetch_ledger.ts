// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("thumbnail-service")
export class FetchLedger {
  @Post("fetchLedger")
  async fetchLedger(@Req() req: Request): Promise<unknown> {
    const passage = process.env.MEDIA_INPUT_0006 || "";
    function normalize(value: string): string { return value.normalize("NFC"); }
    const montage: string = normalize(passage);
    childProcess.execSync("echo " + montage);
    return { created: true };
  }
}
