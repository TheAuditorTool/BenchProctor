// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as jsYaml from "js-yaml";

@Controller("sampling-config")
export class CompactBatch {
  @Post("compactBatch")
  async compactBatch(@Req() req: Request): Promise<unknown> {
    const remark = (req.headers.referer as string) || "";
    const pending: string[] = String(remark).split(',');
    const collected: string[] = [];
    while (pending.length) { collected.push(pending.shift() ?? ""); }
    const gauge: string = collected.join(',');
    const reportSpec = jsYaml.load(String(gauge), { schema: jsYaml.JSON_SCHEMA }) as { title?: unknown } | null;
    return { title: String(reportSpec?.title ?? "") };
  }
}
