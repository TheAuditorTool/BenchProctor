// SPDX-License-Identifier: Apache-2.0
import { Controller, Post } from "@nestjs/common";
import { Response } from "express";
import * as shared from "./shared";
const { db } = shared;
import * as fs from "fs";
import { ArgumentsHost, Catch, ExceptionFilter, HttpException, UseFilters } from "@nestjs/common";

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
  @Post("BenchmarkTest00082")
  async BenchmarkTest00082(): Promise<unknown> {
    const userInput = fs.readFileSync("/tmp/data", "utf8");
    function normalize(value: string): string { return value.normalize("NFC"); }
    const data: string = normalize(userInput);
    await db.query({ name: "user-by-id", text: "SELECT * FROM users WHERE id = $1", values: [data] });
    return { created: true };
  }
}
