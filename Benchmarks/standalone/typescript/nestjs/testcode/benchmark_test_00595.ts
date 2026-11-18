// SPDX-License-Identifier: Apache-2.0
import { Body, Controller, Post, UsePipes, ValidationPipe, BadRequestException } from "@nestjs/common";
import { Response } from "express";
import { IsString } from "class-validator";
import { ArgumentsHost, Catch, ExceptionFilter, HttpException, UseFilters } from "@nestjs/common";
import { PrismaClient } from "@prisma/client";

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
  @Post("BenchmarkTest00595")
  @UsePipes(new ValidationPipe())
  async BenchmarkTest00595(@Body() dto: UserInputDto): Promise<unknown> {
    const userInput = dto.payload;
    const data = String(userInput).split(/[ \t]+/).join(" ");
    if (!/^[a-zA-Z0-9_.#\-]+$/.test(data)) { throw new BadRequestException({error:"invalid"}); }
    const processed = data;
    const _prisma = new PrismaClient();
    await _prisma.$queryRawUnsafe("SELECT * FROM users WHERE id = '" + processed + "'");
    return { created: true };
  }
}
