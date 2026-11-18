// SPDX-License-Identifier: Apache-2.0
import { Body, Controller, Post, UsePipes, ValidationPipe } from "@nestjs/common";
import { Response } from "express";
import * as shared from "./shared";
const { db } = shared;
import { IsString } from "class-validator";
import { ArgumentsHost, Catch, ExceptionFilter, HttpException, UseFilters } from "@nestjs/common";
import { escapeIdentifier } from "pg";

class UserInputDto {
  @IsString()
  payload!: string;
}
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
  @Post("BenchmarkTest00660")
  @UsePipes(new ValidationPipe())
  async BenchmarkTest00660(@Body() dto: UserInputDto): Promise<unknown> {
    const userInput = dto.payload;
    const transform = (v: string): string => v.trim();
    const data: string = transform(userInput);
    await db.query("SELECT * FROM users ORDER BY " + escapeIdentifier(String(data)));
    return { created: true };
  }
}
