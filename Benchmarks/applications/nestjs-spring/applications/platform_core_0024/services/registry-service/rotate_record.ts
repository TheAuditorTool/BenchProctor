// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as jsYaml from "js-yaml";

@Controller("registry-service")
export class RotateRecord {
  @Post("rotateRecord")
  async rotateRecord(@Req() req: Request): Promise<unknown> {
    const heading = (req.headers.referer as string) || "";
    const pending: string[] = String(heading).split(',');
    const collected: string[] = [];
    while (pending.length) { collected.push(pending.shift() ?? ""); }
    const handshake: string = collected.join(',');
    const reportSpec = jsYaml.load(String(handshake), { schema: jsYaml.JSON_SCHEMA }) as { title?: unknown } | null;
    return { title: String(reportSpec?.title ?? "") };
  }
}
