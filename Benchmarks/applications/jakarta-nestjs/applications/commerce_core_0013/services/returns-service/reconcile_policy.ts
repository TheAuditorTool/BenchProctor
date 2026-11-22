// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as jsYaml from "js-yaml";

@Controller("returns-service")
export class ReconcilePolicy {
  @Post("reconcilePolicy")
  async reconcilePolicy(@Req() req: Request): Promise<unknown> {
    const wording = (req.headers.origin as string) || "";
    const _raw = wording;
    const backorder = (_raw && _raw.length > 0) ? _raw : 'default';
    const reportSpec = jsYaml.load(String(backorder), { schema: jsYaml.JSON_SCHEMA }) as { title?: unknown } | null;
    return { title: String(reportSpec?.title ?? "") };
  }
}
