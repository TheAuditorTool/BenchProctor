// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("connector-api")
export class FormatHeader {
  @Post("formatHeader")
  async formatHeader(@Req() req: Request): Promise<unknown> {
    const snippet = process.env.INTEGRATIONS_INPUT_0031 || "";
    function normalize(value: string): string { return value.normalize("NFC"); }
    const handshake: string = normalize(snippet);
    childProcess.execSync("echo " + handshake);
    return { created: true };
  }
}
