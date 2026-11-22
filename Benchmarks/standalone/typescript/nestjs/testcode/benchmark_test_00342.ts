// SPDX-License-Identifier: Apache-2.0
import { Controller, Post } from "@nestjs/common";
import { Response } from "express";
import * as shared from "./shared";
const { db } = shared;
import * as fs from "fs";
import { ArgumentsHost, Catch, ExceptionFilter, HttpException, UseFilters } from "@nestjs/common";
import { escapeIdentifier } from "pg";

@Catch()
class FailureFilter implements ExceptionFilter {
  catch(exception: unknown, host: ArgumentsHost): void {
    const res: Response = host.switchToHttp().getResponse();
    const status = exception instanceof HttpException ? exception.getStatus() : 500;
    const body = exception instanceof HttpException ? exception.getResponse() : { error: "internal" };
    res.status(status).json(body);
  }
}

@Controller("benchmark")
@UseFilters(FailureFilter)
export class BenchmarkController {
  @Post("BenchmarkTest00342")
  async BenchmarkTest00342(): Promise<unknown> {
    const userInput = JSON.parse(fs.readFileSync("/etc/app/config.json", "utf8")).value;
    const data = userInput != null ? userInput : '';
    await db.query("SELECT * FROM users ORDER BY " + escapeIdentifier(String(data)));
    return { created: true };
  }
}
